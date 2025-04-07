# Use the Plot struct as it is provided
defmodule Plot do
  @enforce_keys [:plot_id, :registered_to]
  defstruct [:plot_id, :registered_to]
end

defmodule CommunityGarden do
  @moduledoc """
  Agent
  The Agent module facilitates an abstraction for spawning processes and the receive-send loop.
  From here, we will call processes started using the Agent module 'agent processes'.
  An agent process might be chosen to represent a central shared state.

  To start an agent process, Agent provides the start/2 function.
  The supplied function when start-ing the agent process returns the initial state of the process:

  # Start an agent process with an initial value of an empty list
  {:ok, agent_pid} = Agent.start(fn -> [] end)
  # => {:ok, #PID<0.112.0>}
  Just like Map or List, Agent provides many functions for working with agent processes.

  It is customary to organize and encapsulate all Agent-related functionality into a module for the domain being modeled.
  """
  @spec start(list()) :: {:ok, list()}
  def start(opts \\ []) do
    {:ok, agent_pid} = Agent.start(fn -> {1, opts} end)
  end

  @spec list_registrations(pid()) :: list()
  def list_registrations(pid) do
    Agent.get(pid, fn {_next_id, plots} ->
      Enum.reverse(plots)
    end)
  end

  @spec register(pid(), String.t()) :: Plot.t()
  def register(pid, name) do
    Agent.get_and_update(pid, fn {next_id, plots} ->
      new_plot = %Plot{plot_id: next_id, registered_to: name}
      {new_plot, {next_id + 1, [new_plot | plots]}}
    end)
  end

  @spec release(pid(), integer()) :: :ok
  def release(pid, plot_id) do
    Agent.update(pid, fn {next_id, plots} ->
      updated_plots = Enum.reject(plots, fn %Plot{plot_id: id} -> id == plot_id end)
      {next_id, updated_plots}
    end)
  end

  @spec get_registration(pid(), integer()) :: Plot.t() | {:not_found, String.t()}
  def get_registration(pid, plot_id) do
    Agent.get(pid, fn {_next_id, plots} ->
      case Enum.find(plots, fn %Plot{plot_id: id} -> id == plot_id end) do
        nil -> {:not_found, "plot is unregistered"}
        plot -> plot
      end
    end)
  end
end
