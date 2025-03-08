defmodule Learning do
  @moduledoc """
  Documentation for `Learning`.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Learning.hello()
      :world

  """
  use Application

  @x 5 # works like a constant - immutable variable

  alias UUID

  def start(_type, _args) do
    # code
    Learning.main()
    # execution
    Supervisor.start_link([], strategy: :one_for_one) # works so that you can just run without specifying function
  end

  def main do
    y = 10
    IO.puts(@x + y)
    IO.puts(:hello) # static ATOMS -> constant value that is hardcoded. not good for user input
    IO.puts(Learning.moreStringExample())
  end

  def stringExample do
    name = "Anna"
    # https://hexdocs.pm/elixir/Enum.html
    status = Enum.random([:gold, :silver, :bronze])

    if status == :gold do
      IO.puts("Welcome to gold status, #{name}")
    else
      IO.puts("Get lost") # returns ok as well because no explicit return value in this function
    end
  end

  def caseExample do # example on cases
    name = "Anna"
    status = Enum.random([:gold, :silver, :bronze])
    case status do
      :gold -> IO.puts("Welcome to gold status, #{name}")
      :silver -> IO.puts("Welcome to silver status, #{name}")
      _ -> IO.puts("The rest of the cases here")
    end
  end

  def moreStringExample do
    # https://hexdocs.pm/elixir/String.html
    IO.puts("This\nis\na\nmessage\n")
    IO.puts("After")
    IO.puts("Interpolation looks like \#{}") # quite literally puts #{}
    IO.puts(?a) # value of 97 -> character value
  end
end
