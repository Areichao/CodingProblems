defmodule LanguageList do
  @moduledoc """
  Lists!!

  Elixir implements lists as a linked list, where each node stores two values: the first item and another list with all the remaining items.
  The first item in the list is referred to as the head and the remaining list of items is called the tail.

  # [1] represented in [head | tail] notation
  [1 | []]

  # [1, 2, 3] represented in [head | tail] notation
  [1 | [2 | [3 | []]]]

  We can use [head | tail] notation to prepend elements to a list:

  # Suppose
  list = [2, 1]

  [3, 2, 1] == [3 | list]
  # => true
  """
  @spec new() :: list()
  def new(), do: []

  @doc """
  add an element into the list
  """
  # or just do [language | list]
  def add(list, language), do: [language] ++ list

  @doc """
  return list without first element
  """
  def remove(list) do
    # split into head and tail
    case list do
      [_ | tail] -> tail
      # splitting causes an error in cases of empty lists, so have this as backup
      [] -> []
    end
  end

  @doc """
  takes the first element in a list
  """
  # in this case, split variable at function parameter and return first element
  def first([head | _]), do: head

  def count(list), do: length(list)

  def functional_list?(list), do: "Elixir" in list
end
