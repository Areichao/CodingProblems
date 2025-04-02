defmodule Secrets do
  @moduledoc """
  Anonymous function beginner tutorial (elixir)
  """

  @doc """
  Function calls an anonymous function to add secret to another integer

  user .(num) to invoke param for anonymous function\
  or variable.(num) if anonymous function is set to a variable

  ## Example test case
    add = Secrets.secret_add(4)
    assert add.(3) === 7
  """
  @spec secret_add(integer()) :: (integer() -> integer())
  def secret_add(secret) do
    fn num -> num + secret end
  end

  @spec secret_subtract(integer) :: (integer() -> integer())
  def secret_subtract(secret), do: fn num -> num - secret end

  def secret_multiply(secret), do: fn num -> num * secret end

  def secret_divide(secret), do: fn num -> trunc(num / secret) end

  def secret_and(secret), do: fn num -> Bitwise.band(num, secret) end

  def secret_xor(secret), do: fn num -> Bitwise.bxor(num, secret) end

  @doc """
  return a function which takes one argument and applies to it the two functions passed in to secret_combine in order
  """
  @spec secret_combine((integer() -> integer()), (integer() -> integer())) :: (integer() ->
                                                                                 integer())
  def secret_combine(secret_function1, secret_function2) do
    # pipe num into function 1, and result of function 1 into function 2
    fn num -> num |> secret_function1.() |> secret_function2.() end
  end
end
