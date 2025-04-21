defmodule TopSecret do
  @moduledoc """
  AST
  The Abstract Syntax Tree (AST), also called a quoted expression, is a way to represent code as data.

  Each node in the AST is a three-element tuple.

  # AST representation of:
  # 2 + 3
  {:+, [], [2, 3]}
  The first element, an atom, is the operation. The second element, a keyword list, is the metadata.
  The third element is a list of arguments, which contains other nodes.
  Literal values such as integers, atoms, and strings are represented in the AST as themselves instead of three-element tuples.

  Turning code into ASTs
  Changing Elixir code to ASTs and ASTs back to code is part of the standard library.
  You can find functions for working with ASTs in the modules Code (e.g. to change a string with code to an AST)
  and Macro (e.g. to traverse the AST or change it to a string).

  Note that all of the functions in the standard library use the name "quoted" to mean the AST (short for quoted expression).

  The special form for turning code into an AST is called quote. It accepts a code block and returns its AST.

  quote do
    2 + 3 - 1
  end

  # => {:-, [], [
  #      {:+, [], [2, 3]},
  #      1
  #    ]}
  Use cases
  The ability to represent code as an AST is at the heart of metaprogramming in Elixir.
  Macros, which is a way to write Elixir code that produces Elixir code, work by returning ASTs as output.

  Another use case for ASTs is static code analysis, like Exercism's own tool, the Analyzer,
  which you might already know as the little bot that leaves comments on your solutions.
  """
  def to_ast(string) do
    {:ok, ast} = Code.string_to_quoted(string)
    ast
  end

  def decode_secret_message_part({operation, meta, [{name, _, args_} = head | tail]} = ast, acc)
      when operation in [:def, :defp] and is_atom(name) do
    {ast, [Atom.to_string(name) | acc]}
  end

  def decode_secret_message_part(ast, acc) do
    {ast, acc}
  end

  def decode_secret_message(string) do
    # Please implement the decode_secret_message/1 function
  end
end
