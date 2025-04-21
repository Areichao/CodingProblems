defmodule LogParser do
  @moduledoc """
  Regular Expressions
  Regular expressions in Elixir follow the PCRE specification (Perl Compatible Regular Expressions),
  similarly to other popular languages like Java, JavaScript, or Ruby.

  The Regex module offers functions for working with regular expressions.
  Some of the String module functions accept regular expressions as arguments as well.

  Note
  This exercise assumes that you already know regular expression syntax, including character classes, quantifiers, groups, and captures.

  If you need a refresh your regular expression knowledge, check out one of those sources: Regular-Expressions.info, Rex Egg, RegexOne, Regular Expressions 101, RegExr.

  Sigils
  The most common way to create regular expressions is using the ~r sigil.

  ~r/test/
  Note that all Elixir sigils support different kinds of delimiters, not only /.

  Matching
  The =~/2 operator can be used to perform a regex match that returns boolean result.
  Alternatively, there are also match?/2 functions in the Regex module as well as the String module.

  "this is a test" =~ ~r/test/
  # => true

  String.match?("Alice has 7 apples", ~r/\d{2}/)
  # => false
  Capturing
  If a simple boolean check is not enough, use the Regex.run/3 function to get a list of all captures (or nil if there was no match).
  The first element in the returned list is always a match for the whole regular expression, and the following elements are matched groups.

  Regex.run(~r/(\d) apples/, "Alice has 7 apples")
  # => ["7 apples", "7"]
  Modifiers
  The behavior of a regular expression can be modified by appending special flags.
  When using a sigil to create a regular expression, add the modifiers after the second delimiter.

  Common modifiers are:

  i - makes the match case-insensitive.
  u - enables Unicode specific patterns like \p and causes character classes like \w, \s etc. to also match Unicode.
  "this is a TEST" =~ ~r/test/i
  # => true
  """
  def valid_line?(line) do
    Regex.match?(~r/^\[(DEBUG|INFO|WARNING|ERROR)\]/, line)
  end

  def split_line(line) do
    Regex.split(~r/<[-~=*]*>/, line)
  end

  def remove_artifacts(line) do
    Regex.replace(~r/end-of-line\d+/i, line, "")
  end

  def tag_with_user_name(line) do
    case Regex.run(~r/User\s+(\S+)/, line) do
      [_, username] -> "[USER] #{username} " <> line
      _ -> line
    end
  end
end
