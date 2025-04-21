defmodule LucasNumbers do
  @moduledoc """
  Lucas numbers are an infinite sequence of numbers which build progressively
  which hold a strong correlation to the golden ratio (φ or ϕ)

  E.g.: 2, 1, 3, 4, 7, 11, 18, 29, ...

  Streams
  All functions in the Enum module are eager.
  When performing multiple operations on enumerables with the Enum module, each operation is going to generate an intermediate result.

  The Stream module is a lazy alternative to the eager Enum module.
  It offers many of the same functions as Enum, but instead of generating intermediate results,
  it builds a series of computations that are only executed once the stream is passed to a function from the Enum module.

  Streams implement the Enumerable protocol and are composable -- you can chain them together to create more complex functionality.
  """
  @spec generate(integer()) :: list(integer())
  # when code is nawt good
  def generate(count) when not is_integer(count) or count < 1 do
    raise ArgumentError, message: "count must be specified as an integer >= 1"
  end

  def generate(1), do: [2]
  def generate(2), do: [2, 1]

  def generate(count) do
    generate(2)
    |> Stream.unfold(fn [a, b] -> {a, [b, a + b]} end)
    |> Enum.take(count)
  end
end
