defmodule Username do
  @moduledoc"""
  Charlists!

  ~c"hello" or 'hello' in older versions of elixir
  list of integers

  ?A
  # => 65

  [?:, ?)]
  # => ~c":)"
  """
  # base case
  def sanitize(~c""), do: ~c""
  def sanitize([head|tail]) when (head >= ?a and head <= ?z) or head == ?_, do: [head | Username.sanitize(tail)]
  def sanitize([?ä|tail]), do: ~c"ae" ++ Username.sanitize(tail)
  def sanitize([?ö|tail]), do: ~c"oe" ++ Username.sanitize(tail)
  def sanitize([?ü|tail]), do: ~c"ue" ++ Username.sanitize(tail)
  def sanitize([?ß|tail]), do: ~c"ss" ++ Username.sanitize(tail)
  def sanitize([_head|tail]), do: Username.sanitize(tail)
    # ä becomes ae
    # ö becomes oe
    # ü becomes ue
    # ß becomes ss

    # Please implement the sanitize/1 function
end
