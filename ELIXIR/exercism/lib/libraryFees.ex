defmodule LibraryFees do
  @moduledoc """
  Date and Time module

  The Date module. A Date struct can be created with the ~D sigil.
  ~D[2021-01-01]

  The Time module. A Time struct can be created with the ~T sigil.
  ~T[12:00:00]

  The NaiveDateTime module for datetimes without a timezone. A NaiveDateTime struct can be created with the ~N sigil.
  ~N[2021-01-01 12:00:00]

  Comparisons
  To compare dates or times to one another, look for a compare or diff function in the corresponding module.
  Comparison operators such as ==, >, and < seem to work, but they don't do a correct semantic comparison for those structs.
  """
  def datetime_from_string(string) do
    string |> DateTime.from_iso8601() |> elem(1) |> DateTime.to_naive()
  end

  def before_noon?(%NaiveDateTime{hour: hour}), do: hour < 12

  def return_date(checkout_datetime) do
    if LibraryFees.before_noon?(checkout_datetime) do
      # takes in number of seconds as argument
      NaiveDateTime.to_date(NaiveDateTime.add(checkout_datetime, 28 * 24 * 60 * 60))
    else
      NaiveDateTime.to_date(NaiveDateTime.add(checkout_datetime, 29 * 24 * 60 * 60))
    end
  end

  def days_late(planned_return_date, actual_return_datetime) do
    # since we only care about the date and not the time we can convert the thing to just Date
    actual_return_date = NaiveDateTime.to_date(actual_return_datetime)

    # :gt atom is returned since the actual return date is later (greater than) planned return date
    if Date.compare(actual_return_date, planned_return_date) == :gt do
      Date.diff(actual_return_date, planned_return_date)
    else
      0
    end
  end

  def monday?(datetime) do
    # day of week module is in Date so we convert. 1 represents monday
    NaiveDateTime.to_date(datetime) |> Date.day_of_week() == 1
  end

  def calculate_late_fee(checkout, return, rate) do
    checkout = LibraryFees.datetime_from_string(checkout)
    return = LibraryFees.datetime_from_string(return)
    num_late_days = LibraryFees.days_late(LibraryFees.return_date(checkout), return)

    if LibraryFees.monday?(return) do
      div(num_late_days * rate, 2)
    else
      num_late_days * rate
    end
  end
end
