defmodule BirdCount do
  @moduledoc """
  recursion

  Very often, each case is written in its own function clause.

  # base case
  def count([]), do: 0

  # recursive case
  def count([_head | tail]), do: 1 + count(tail)
  """
  @spec today(list()) :: integer()
  def today(list), do: Enum.at(list, 0)

  @spec increment_day_count(list()) :: list()
  def increment_day_count(list) do
    today = BirdCount.today(list)

    case today do
      nil ->
        [1]

      _ ->
        [_head | tail] = list
        [today + 1 | tail]
    end
  end

  # Iterative: Enum.any?(list, &(&1 == 0)) # & is anonymous function, does fn x -> x == 0 end
  # Recursive method
  @spec has_day_without_birds?(list()) :: boolean()
  def has_day_without_birds?([]), do: false
  def has_day_without_birds?([0 | _tail]), do: true
  def has_day_without_birds?([_head | tail]), do: BirdCount.has_day_without_birds?(tail)

  # Iterative: Enum.sum(list)
  # Recursive method
  @spec total(list()) :: integer()
  def total([]), do: 0
  def total([head | tail]), do: head + BirdCount.total(tail)

  @spec busy_days(list()) :: integer()
  def busy_days([]), do: 0
  def busy_days([head | tail]) when head >= 5, do: 1 + BirdCount.busy_days(tail)
  def busy_days([_head | tail]), do: BirdCount.busy_days(tail)
end
