defmodule RPG.CharacterSheet do
  @moduledoc"""
  IO module for IO inputs and outputs

  Output
  To write a string to the standard output, use IO.puts.
  IO.puts always adds a new line at the end of the string.
  If you don't want that behavior, use IO.write instead.
  Both functions return the atom :ok if they succeed.

  IO.puts("Hi!")
  # > Hi!
  # => :ok

  IO.puts is useful for writing strings, but not much else.
  If you need a tool for debugging that will allow you to write any value to standard output, use IO.inspect instead.
  IO.inspect returns the value it was passed unchanged, so it can be inserted in any point in your code.
  It also accepts many options, for example :label, that will allow you to distinguish it from other IO.inspect calls.

  Input
  To read a line from the standard input, use IO.gets.
  IO.gets accepts one argument - a string that it will print as a prompt for the input.
  IO.gets doesn't add a new line after the prompt, include it yourself if you need it.

  IO.gets("What's your name?\n")
  # > What's your name?
  # < Mary
  # => "Mary\n"
  """
  @spec welcome() :: :ok
  def welcome() do
    IO.puts("Welcome! Let's fill out your character sheet together.")
  end

  @spec ask_name() :: String.t()
  def ask_name(), do: String.trim(IO.gets("What is your character's name?\n"))

  def ask_class(), do: String.trim(IO.gets("What is your character's class?\n"))

  def ask_level(), do: String.to_integer(String.trim(IO.gets("What is your character's level?\n")))

  @spec run() :: :ok
  def run() do
    RPG.CharacterSheet.welcome()
    name = RPG.CharacterSheet.ask_name()
    class = RPG.CharacterSheet.ask_class()
    level = RPG.CharacterSheet.ask_level()
    charMap = %{class: class, name: name, level: level}
    IO.inspect(charMap, label: "Your character")
  end
end
