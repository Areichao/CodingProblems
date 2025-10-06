defmodule PaintByNumber do
  @moduledoc """
  Bitstrings

  Working with binary data is an important concept in any language,
  and Elixir provides an elegant syntax to write, match, and construct binary data.

  In Elixir, binary data is referred to as the bitstring type.
  The binary data type (not to be confused with binary data in general) is a specific form of a bitstring,
  which we will discuss in a later exercise.

  Bitstring literals are defined using the bitstring special form <<>>.
  When defining a bitstring literal, it is defined in segments.
  Each segment has a value and type, separated by the :: operator.
  The type specifies how many bits will be used to encode the value.
  The type can be omitted completely, which will default to a 8-bit integer value.

  # This defines a bitstring with three segments of a single bit each
  <<0::1, 1::1, 0::1>>
  Specifying the type as ::1 is a shorthand for writing ::size(1).
  You need to use the longer syntax if the bit size comes from a variable.

  Binary
  When writing binary integer literals, we can write them directly in base-2 notation by prefixing the literal with 0b.
  Note that they will be anyway displayed as decimal numbers when printed in tests results or when using iex.

  <<0b1011::4>> == <<11::4>>
  # => true

  Truncating
  If the value of the segment overflows the capacity of the segment's type, it will be truncated from the left.

  <<0b1011::3>> == <<0b0011::3>>
  # => true

  Prepending and appending
  You can both prepend and append to an existing bitstring using the special form.
  The ::bitstring type must be used on the existing bitstring if it's of unknown size.

  value = <<0b110::3, 0b001::3>>
  new_value = <<0b011::3, value::bitstring, 0b000::3>>
  # => <<120, 8::size(4)>>

  Concatenating
  We can concatenate bitstrings stored in variables using the special form.
  The ::bitstring type must be used when concatenating two bitstrings of unknown sizes.

  first = <<0b110::3>>
  second = <<0b001::3>>
  concatenated = <<first::bitstring, second::bitstring>>
  # => <<49::size(6)>>

  Pattern matching
  Pattern matching can also be done to obtain values from the special form.
  You have to know the number of bits for each fragment you want to capture,
  with one exception: the ::bitstring type can be used to pattern match on a bitstring of an unknown size,
  but this can only be used for the last fragment.

  <<value::4, rest::bitstring>> = <<0b01101001::8>>
  value == 0b0110
  # => true
  """

  # BASE CASE
  def palette_bit_size(color_count), do: bit_size_helper(color_count, 0)

  # helper function
  defp bit_size_helper(color_count, n) do
    # do edge case for one bit
    if 2 ** n >= color_count do
      n
    else
      bit_size_helper(color_count, n + 1)
    end
  end

  def empty_picture() do
    <<>>
  end

  def test_picture() do
    <<00::2, 01::2, 10::2, 11::2>>
  end

  def prepend_pixel(picture, color_count, pixel_color_index) do
    number_bits = PaintByNumber.palette_bit_size(color_count)
    <<pixel_color_index::size(number_bits), picture::bitstring>>
  end

  def get_first_pixel(picture, color_count) do
    num_bits = PaintByNumber.palette_bit_size(color_count)

    if picture == PaintByNumber.empty_picture() do
      nil
    else
      <<first::size(num_bits), _rest::bitstring>> = picture
      first
    end
  end

  def drop_first_pixel(picture, color_count) do
    if picture == <<>> do
      PaintByNumber.empty_picture()
    else
      num_bits = PaintByNumber.palette_bit_size(color_count)
      <<_first::size(num_bits), rest::bitstring>> = picture
    end
  end

  @spec concat_pictures(bitstring(), bitstring()) :: bitstring()
  def concat_pictures(picture1, picture2) do
    <<picture1::bitstring, picture2::bitstring>>
  end
end
