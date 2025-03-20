defmodule HighSchoolSweetheart do
  @moduledoc"""
  Strings stuff

  "Welcome to" <> " " <> "New York"
  # => "Welcome to New York"

  "6 * 7 = #{6 * 7}"
  # => "6 * 7 = 42"

  """
  @spec first_letter(String.t()) :: String.t()
  def first_letter(name), do: String.trim(name) |> String.first()

  def initial(name), do: String.upcase(HighSchoolSweetheart.first_letter(name)) <> "."

  def initials(full_name) do
    names = String.split(full_name) # splits on whitespace by default
    HighSchoolSweetheart.initial(Enum.at(names, 0)) <> " " <> HighSchoolSweetheart.initial(Enum.at(names, 1))
  end

  def pair(full_name1, full_name2) do
    """
    ❤-------------------❤
    |  #{HighSchoolSweetheart.initials(full_name1)}  +  #{HighSchoolSweetheart.initials(full_name2)}  |
    ❤-------------------❤
    """
  end
end
