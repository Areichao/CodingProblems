defmodule DNA do
  @moduledoc """
    Accumulators should be initialized by the function's author, not the function's user.
    To achieve this, declare two functions - a public function that takes just the necessary data as arguments and initializes the accumulator,
    and a private function that also takes an accumulator.
    In Elixir, it is a common pattern to prefix the private function's name with do_.

    # Count the length of a list without an accumulator
    def count([]), do: 0
    def count([_head | tail]), do: 1 + count(tail)

    # Count the length of a list with an accumulator
    def count(list), do: do_count(list, 0)

    defp do_count([], count), do: count
    defp do_count([_head | tail], count), do: do_count(tail, count + 1)

    The usage of an accumulator allows us to turn recursive functions into tail-recursive functions.
    A function is tail-recursive if the last thing executed by the function is a call to itself.
  """

  @nuclear_map %{?\s => 0, ?A => 1, ?C => 2, ?G => 4, ?T => 8}
  def encode_nucleotide(code_point) do
    Map.get(@nuclear_map, code_point)
  end

  def decode_nucleotide(encoded_code) do
    {key, _value} = Enum.find(@nuclear_map, fn {_k, v} -> v == encoded_code end)
    key
  end

  def encode(dna) do
    do_encode(dna, <<>>)
  end

  defp do_encode([], bitstring_val), do: bitstring_val

  defp do_encode([head | rest], bitstring_val) do
    binary_data = DNA.encode_nucleotide(head)
    do_encode(rest, <<bitstring_val::bitstring, binary_data::4>>)
  end

  def decode(dna) do
    do_decode(dna, ~c"")
  end

  defp do_decode(<<>>, charlist), do: charlist

  defp do_decode(<<value::4, rest::bitstring>>, charlist) do
    do_decode(rest, charlist ++ [DNA.decode_nucleotide(value)])
  end
end
