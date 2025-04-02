defmodule Exercism do
  use Application

  @moduledoc """
  Documentation for `Exercism`.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Exercism.hello()
      :world

  """
  @impl true
  def start(_type, _args) do
    # code
    main()
    # execution
    # works so that you can just run without specifying function
    Supervisor.start_link([], strategy: :one_for_one)
  end

  def main do
    IO.inspect(Exercism.hello())
  end

  @spec hello() :: String.t()
  def hello do
    "Hello World"
  end
end
