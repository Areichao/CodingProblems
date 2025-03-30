defmodule BasketballWebsite do
  @moduledoc """
  Access Behaviour
  Elixir uses code Behaviours to provide common generic interfaces while facilitating specific implementations for each module which implements it.
  One such common example is the Access Behaviour.

  The Access Behaviour provides a common interface for retrieving data from a key-based data structure.
  The Access Behaviour is implemented for maps and keyword lists, but let's look at its use for maps to get a feel for it.
  Access Behaviour specifies that when you have a map, you may follow it with square brackets and then use the key to retrieve
  the value associated with that key.

  # Suppose we have these two maps defined (note the difference in the key type)
  my_map = %{key: "my value"}
  your_map = %{"key" => "your value"}

  # Obtain the value using the Access Behaviour
  my_map[:key] == "my value"
  your_map[:key] == nil
  your_map["key"] == "your value"

  If the key does not exist in the data structure, then nil is returned.
  This can be a source of unintended behavior, because it does not raise an error.
  Note that nil itself implements the Access Behaviour and always returns nil for any key.
  """
  def extract_from_path(_data, ""), do: nil
  def extract_from_path(data, path) do
    [head|tail] = String.split(path, ".")
    case tail do
      [] ->
        data[head]
      _ ->
        if data[head] != nil do
          BasketballWebsite.extract_from_path(data[head], Enum.join(tail, "."))
        else
          nil
        end
    end
  end

  def get_in_path(data, path) do
    get_in(data, String.split(path, "."))
  end
end
