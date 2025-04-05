defmodule Chessboard do
  @moduledoc """
  Ranges
  Ranges represent a sequence of one or many consecutive integers. They are created by connecting two integers with ...

  1..5
  Ranges can be ascending or descending. They are always inclusive of the first and last values.

  A range implements the Enumerable protocol, which means functions in the Enum module can be used to work with ranges.
  """
  @spec rank_range :: Range.t()
  def rank_range, do: 1..8

  def file_range, do: ?A..?H

  def ranks, do: Enum.to_list(Chessboard.rank_range())

  def files, do: Enum.map(Chessboard.file_range(), fn code -> <<code>> end)
end
