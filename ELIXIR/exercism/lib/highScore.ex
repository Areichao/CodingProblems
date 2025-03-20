defmodule HighScore do
  @moduledoc"""
  Maps

  # If the key is an atom:
  %{atom_key: 1}

  # If the key is a different type:
  %{1 => :atom_value}

  # You can even mix these if the atom form comes second:
  %{"first_form" => :a, atom_form: :b}

  map = %{a: 1, b: 2}
  new_map = %{map | b: 20, c: 3}

  IO.inspect(new_map)
  # %{a: 1, b: 20, c: 3}

  Constants
  you can define constants at the start of each module like
  @constant_number 1
  """

  @initial_score 0

  @spec new() :: map()
  def new(), do: %{}

  def add_player(scores, name, score \\ @initial_score), do: Map.put(scores, name, score)

  def remove_player(scores, name), do: Map.delete(scores, name)

  def reset_score(scores, name), do: Map.put(scores, name, @initial_score)

  # Maps.get() ensures that a missing key will put 0 unlike just doing scores[key]
  def update_score(scores, name, score), do: Map.update(scores, name, score, &(&1 + score))

  def get_players(scores), do: Map.keys(scores)
end
