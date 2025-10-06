defmodule Lasagna do
  @moduledoc """
  Lasagna timer rules for learning elixir module 2
  """
  # Please define the 'expected_minutes_in_oven/0' function
  @doc """
  How long lasagna should be in the oven for
  ## Examples
    iex> Lasagna.expected_minutes_in_oven()
    40
  """
  @spec expected_minutes_in_oven() :: integer()
  # shortened one line functions, defp for private functions
  def expected_minutes_in_oven(), do: 40

  # Please define the 'remaining_minutes_in_oven/1' function
  @doc """
  How much longer lasagna has to be in the oven
  ## Examples
    iex> Lasagna.remaining_minutes_in_oven(10)
    30
  """
  @spec remaining_minutes_in_oven(integer()) :: integer()
  def remaining_minutes_in_oven(in_oven), do: Lasagna.expected_minutes_in_oven() - in_oven

  # Please define the 'preparation_time_in_minutes/1' function
  @doc """
  How long it took to prepare (2 mins per layer)
  ## Examples
    iex> Lasagna.preparation_time_in_minutes(10)
    20
  """
  @spec preparation_time_in_minutes(integer()) :: integer()
  def preparation_time_in_minutes(number_layers), do: number_layers * 2

  # Please define the 'total_time_in_minutes/2' function
  @doc """
  How long youve worked on it so far (layers + time in oven)
  ## Examples
    iex> Lasagna.total_time_in_minutes(10, 10)
    30
  """
  @spec total_time_in_minutes(integer(), integer()) :: integer()
  def total_time_in_minutes(number_layers, in_oven), do: number_layers * 2 + in_oven

  # Please define the 'alarm/0' function

  @doc """
  Returns an alarm sound.

  ## Examples

      iex> Lasagna.alarm()
      "Ding!"

  """
  @spec alarm() :: String.t()
  def alarm(), do: "Ding!"
end
