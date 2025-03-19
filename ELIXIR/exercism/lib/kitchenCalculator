defmodule KitchenCalculator do
  @moduledoc"""
  Tuples - {}
  and pattern matching using =
  2 = 2
  # => 2
  # Literals can be matched if they are the same

  2 = 3
  # => ** (MatchError) no match of right hand side value: 3

  {_, denominator} = Float.ratio(0.25)
  # => {1, 4}
  # the variable `denominator` is bound to the value 4

  setting variables

  defmodule Example do
  def named_function(:a = variable_a) do
    {variable_a, 1}
  end

  def named_function(:b = variable_b) do
    {variable_b, 2}
  end
  end
  """
  @spec get_volume(tuple()) :: float()
  def get_volume({_, num}), do: num

  def to_milliliter({unit, volume}) do
    case unit do
      :cup -> {:milliliter, volume*240}
      :fluid_ounce -> {:milliliter, volume*30}
      :teaspoon -> {:milliliter, volume*5}
      :tablespoon -> {:milliliter, volume*15}
      _ -> {:milliliter, volume}
    end
  end

  def from_milliliter(volume_pair, unit) do
    {_, volume} = volume_pair
    case unit do
      :cup -> {unit, volume/240}
      :fluid_ounce -> {unit, volume/30}
      :teaspoon -> {unit, volume/5}
      :tablespoon -> {unit, volume/15}
      _ -> {:milliliter, volume}
    end
  end

  def convert(volume_pair, unit) do
    milli = KitchenCalculator.to_milliliter(volume_pair)
    result = KitchenCalculator.from_milliliter(milli, unit)
  end
end
