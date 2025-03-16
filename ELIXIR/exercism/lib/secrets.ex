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

  def secret_subtract(secret) do
    # Please implement the secret_subtract/1 function
  end

  def secret_multiply(secret) do
    # Please implement the secret_multiply/1 function
  end

  def secret_divide(secret) do
    # Please implement the secret_divide/1 function
  end

  def secret_and(secret) do
    # Please implement the secret_and/1 function
  end

  def secret_xor(secret) do
    # Please implement the secret_xor/1 function
  end

  def secret_combine(secret_function1, secret_function2) do
    # Please implement the secret_combine/2 function
  end
end
