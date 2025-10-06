defmodule RPNCalculatorInspection do
  @moduledoc """
    Links
    Elixir processes are isolated and don't share anything by default.
    When an unlinked child process crashes, its parent process is not affected.

    This behavior can be changed by linking processes to one another.
    If two processes are linked, a failure in one process will be propagated to the other process.
    Links are bidirectional.

    Processes can be spawned already linked to the calling process using spawn_link/1 which is an atomic operation,
    or they can be linked later with Process.link/1.

    Linking processes can be useful when doing parallelized work when each chunk of work shouldn't be continued in case another chunk fails to finish.

    Trapping exits
    Linking can also be used for supervising processes.
    If a process traps exits, it will not crash when a process to which it's linked crashes.
    It will instead receive a message about the crash.
    This allows it to deal with the crash gracefully, for example by restarting the crashed process.

    A process can be configured to trap exits by calling Process.flag(:trap_exit, true).
    Note that Process.flag/2 returns the old value of the flag, not the new one.

    The message that will be sent to the process in case a linked process crashes will match the pattern {:EXIT, from, reason},
    where from is a PID. If reason is anything other than the atom :normal, that means that the process crashed or was forcefully killed.

    Tasks
    Tasks are processes meant to execute one specific operation.
    They usually don't communicate with other processes, but they can return a result to the process that started the task.

    Tasks are commonly used to parallelize work.

    async/await
    To start a task, use Task.async/1.
    It takes an anonymous function as an argument and executes it in a new process that is linked to the caller process.
    It returns a %Task{} struct.

    To get the result of the execution, pass the %Task{} struct to Task.await/2.
    It will wait for the task to finish and return its result. The second argument is a timeout in milliseconds, defaulting to 5000.

    Note that between starting the task and awaiting the task, the process that started the task is not blocked and might do other operations.

    Any task started with Task.async/1 should be awaited because it will send a message to the calling process.
    Task.await/2 can be called for each task only once.

    start/start_link
    If you want to start a task for side-effects only, use Task.start/1 or Task.start_link/1.
    Task.start/1 will start a task that is not linked to the calling process,
    and Task.start_link/1 will start a task that is linked to the calling process. Both functions return a {:ok, pid} tuple.
  """

  @spec start_reliability_check((any() -> any()), any()) :: %{input: any(), pid: pid()}
  def start_reliability_check(calculator, input) do
    pid = spawn_link(fn -> calculator.(input) end)
    %{input: input, pid: pid}
  end

  @spec await_reliability_check_result(%{pid: pid(), input: String.t()}, map()) :: map()
  def await_reliability_check_result(%{pid: pid, input: input}, results) do
    receive do
      {:EXIT, ^pid, :normal} -> Map.put(results, input, :ok)
      {:EXIT, ^pid, _anyReason} -> Map.put(results, input, :error)
    after
      100 -> Map.put(results, :input, :timeout)
    end
  end

  @spec reliability_check((any() -> any()), [String.t()]) :: map()
  def reliability_check(calculator, inputs) do
    # save the original trap exit flag
    og_flag = Process.flag(:trap_exit, true)

    try do
      inputs
      |> Enum.map(&start_reliability_check(calculator, &1))
      |> Enum.reduce(%{}, fn check_info, acc ->
        await_reliability_check_result(check_info, acc)
      end)
    after
      # restore original flag value
      Process.flag(:trap_exit, og_flag)
    end
  end

  @spec correctness_check((any() -> any()), [String.t()]) :: [any()]
  def correctness_check(calculator, inputs) do
    inputs
    |> Enum.map(fn input ->
      Task.async(fn -> calculator.(input) end)
    end)
    |> Enum.map(fn task ->
      Task.await(task, 100)
    end)
  end
end
