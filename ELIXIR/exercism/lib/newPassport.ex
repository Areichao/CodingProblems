defmodule NewPassport do
  @moduledoc """
  With
  The special form with provides a way to focus on the "happy path" of a series of potentially failing steps and deal with the failures later.

  with {:ok, id} <- get_id(username),
      {:ok, avatar} <- fetch_avatar(id),
      {:ok, image_type} <- check_valid_image_type(avatar) do
    {:ok, image_type, avatar}
  else
    :not_found ->
      {:error, "invalid username"}

    {:error, "not an image"} ->
      {:error, "avatar associated to #{username} is not an image"}

    err ->
      err
  end
  At each step, if a clause matches, the chain will continue until the do block is executed.
  If one match fails, the chain stops and the non-matching clause is returned.
  You have the option of using an else block to catch failed matches and modify the return value.
  """

  def get_new_passport(now, birthday, form) do
    with {:ok, timestamp} <- enter_building(now),
         {:ok, manual} <- find_counter_information(now),
         counter_number = manual.(birthday),
         {:ok, check_sum} <- stamp_form(timestamp, counter_number, form),
         passport_number = get_new_passport_number(timestamp, counter_number, check_sum) do
      {:ok, passport_number}
    else
      {:error, message} ->
        {:error, message}

      {:coffee_break, _instructions} ->
        retry_time = NaiveDateTime.add(now, 15 * 60, :second)
        {:retry, retry_time}
    end
  end

  # Do not modify the functions below

  defp enter_building(%NaiveDateTime{} = datetime) do
    day = Date.day_of_week(datetime)
    time = NaiveDateTime.to_time(datetime)

    cond do
      day <= 4 and time_between(time, ~T[13:00:00], ~T[15:30:00]) ->
        {:ok, datetime |> DateTime.from_naive!("Etc/UTC") |> DateTime.to_unix()}

      day == 5 and time_between(time, ~T[13:00:00], ~T[14:30:00]) ->
        {:ok, datetime |> DateTime.from_naive!("Etc/UTC") |> DateTime.to_unix()}

      true ->
        {:error, "city office is closed"}
    end
  end

  @eighteen_years 18 * 365
  defp find_counter_information(%NaiveDateTime{} = datetime) do
    time = NaiveDateTime.to_time(datetime)

    if time_between(time, ~T[14:00:00], ~T[14:20:00]) do
      {:coffee_break, "information counter staff on coffee break, come back in 15 minutes"}
    else
      {:ok, fn %Date{} = birthday -> 1 + div(Date.diff(datetime, birthday), @eighteen_years) end}
    end
  end

  defp stamp_form(timestamp, counter, :blue) when rem(counter, 2) == 1 do
    {:ok, 3 * (timestamp + counter) + 1}
  end

  defp stamp_form(timestamp, counter, :red) when rem(counter, 2) == 0 do
    {:ok, div(timestamp + counter, 2)}
  end

  defp stamp_form(_timestamp, _counter, _form), do: {:error, "wrong form color"}

  defp get_new_passport_number(timestamp, counter, checksum) do
    "#{timestamp}-#{counter}-#{checksum}"
  end

  defp time_between(time, from, to) do
    Time.compare(from, time) != :gt and Time.compare(to, time) == :gt
  end
end
