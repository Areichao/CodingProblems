defmodule FreelancerRates do
  @moduledoc """
  8 hour a day work days
  22 working days in a month
  """

  @doc """
  Return the daily rate given hourly rate
  ## Example
    iex> FreelancerRates.daily_rate(60)
    480
  """
  @spec daily_rate(integer()) :: float()
  def daily_rate(hourly_rate), do: hourly_rate * 8.0

  # * 1.0 for float conversion
  @spec apply_discount(integer(), integer()) :: float()
  def apply_discount(before_discount, discount), do: 1.0 * before_discount * (1.0 - discount / 100.0)

  # trunc/1 to truncate it (turn it into an integer)
  @spec monthly_rate(integer(), float()) :: integer()
  def monthly_rate(hourly_rate, discount), do: trunc(Float.ceil(FreelancerRates.apply_discount(FreelancerRates.daily_rate(hourly_rate) * 22, discount)))

  # float floor to one decimal space
  @spec days_in_budget(integer(), integer(), float()) :: integer()
  def days_in_budget(budget, hourly_rate, discount), do: Float.floor(budget / FreelancerRates.apply_discount(FreelancerRates.daily_rate(hourly_rate), discount), 1)
end
