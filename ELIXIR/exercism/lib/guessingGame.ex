defmodule GuessingGame do
  @moduledoc """
  Elixir facilitates Open-Closed Principle practices by allowing functions to have multiple clauses,
  so instead of sprawling and hard-coded control-logic, pointed functions can be written to add/remove behavior easily.

  Elixir offers multiple function clauses and guards to write:

  def number(n) when n == 7 do
    "Awesome, that's my favorite"
  end

  def number(_n) do
    "That's not my favorite"
  end
  """


    @doc """
    Compares a guess to the secret number and returns feedback.

    - Returns `"Correct"` if the guess is exactly the secret number.
    - Returns `"So close"` if the guess is 1 off.
    - Returns `"Too low"` if the guess is lower than the secret number.
    - Returns `"Make a guess"` otherwise.
  """

  @spec compare(integer(), integer() | any()) :: String.t()
  def compare(_secret_number, guess \\ :no_guess) # defaulted to :no_guess if nothing is provided
  def compare(_secret_number, guess) when not is_integer(guess), do: "Make a guess"
  def compare(secret_number, guess) when secret_number == guess, do: "Correct"
  def compare(secret_number, guess) when guess - 1 == secret_number or guess + 1 == secret_number, do: "So close"
  def compare(secret_number, guess) when secret_number > guess, do: "Too low"
  def compare(secret_number, guess) when secret_number < guess, do: "Too high"
end
