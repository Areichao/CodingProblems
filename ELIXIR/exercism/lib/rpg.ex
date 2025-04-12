defmodule RPG do
  @moduledoc """
  Protocols
  Protocols are a mechanism to achieve polymorphism in Elixir when you want behavior to vary depending on the data type.

  Protocols are defined using defprotocol and contain one or more function headers.

  defprotocol Reversible do
    def reverse(term)
  end
  Protocols can be implemented using defimpl.

  defimpl Reversible, for: List do
    def reverse(term) do
      Enum.reverse(term)
    end
  end
  A protocol can be implemented for any existing Elixir data type or for a struct.

  When a protocol function is invoked, the appropriate implementation gets automatically chosen based on the type of the first argument.
  """

  defmodule Character do
    defstruct health: 100, mana: 0

    @type t :: %__MODULE__{
            health: non_neg_integer(),
            mana: non_neg_integer()
          }
  end

  defmodule LoafOfBread do
    defstruct []
  end

  defmodule ManaPotion do
    defstruct strength: 10
  end

  defmodule Poison do
    defstruct []
  end

  defmodule EmptyBottle do
    defstruct []
  end

  # Add code to define the protocol and its implementations below here...
  defprotocol Edible do
    @spec eat(struct(), RPG.Character.t()) :: {struct() | nil, RPG.Character.t()}
    def eat(item, character)
  end
end

defimpl RPG.Edible, for: RPG.LoafOfBread do
  def eat(_item, character) do
    new_character = %RPG.Character{character | health: character.health + 5}
    {nil, new_character}
  end
end

defimpl RPG.Edible, for: RPG.ManaPotion do
  def eat(item, character) do
    new_character = %RPG.Character{character | mana: character.mana + item.strength}
    {%RPG.EmptyBottle{}, new_character}
  end
end

defimpl RPG.Edible, for: RPG.Poison do
  def eat(_item, character) do
    new_character = %RPG.Character{character | health: 0}
    {%RPG.EmptyBottle{}, new_character}
  end
end
