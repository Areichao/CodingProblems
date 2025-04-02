defmodule FileSniffer do
  @moduledoc """
  Binaries
  Elixir provides an elegant syntax for working with binary data as we have seen with the <<>> special form provided for working with bitstrings.

  The binary type is a specialization on the bitstring type.
  Where bitstrings could be of any length (any number of bits), binaries are where the number of bits can be evenly divided by 8.
  That is, when working with binaries, we often think of things in terms of bytes (8 bits).
  A byte can represent integer numbers from 0 to 255. It is common to work with byte values in hexadecimal, 0x00 - 0xFF.

  Binary literals are defined using the bitstring special form <<>>.
  When defining a binary literal, we can use integer and string literals.
  Integer values greater than 255 will overflow and only the last 8 bits of the integer will be used.
  By default, the ::binary modifier is applied to the value. We can concatenate binaries with the <>/2 operator.

  <<255>> == <<0xFF>>
  # Overflowing bits are truncated
  <<256>> == <<0>>
  <<2, 4, 6, 8, 10, 12, 14, 16>> == <<0x02, 0x04, 0x06, 0x08, 0x0A, 0x0C, 0x0E, 0x10>>
  A null-byte is another name for <<0>>.

  Pattern matching on binary data
  Pattern matching is even extended to binaries, and we can pattern match on a portion of binary data much like we could for a list.

  # Ignore the first 8 bytes, match and bind the remaining to `body`
  <<_::binary-size(8), body::binary>>
  Like with other types of pattern matching, we can use this in function signatures to match when selecting from multiple function clauses
  """
  @spec type_from_extension(String.t()) :: String.t() | nil
  def type_from_extension(extension) do
    case extension do
      "exe" -> "application/octet-stream"
      "bmp" -> "image/bmp"
      "png" -> "image/png"
      "jpg" -> "image/jpg"
      "gif" -> "image/gif"
      _ -> nil
    end
  end

  def type_from_binary(file_binary) do
    case file_binary do
      <<0x7F, 0x45, 0x4C, 0x46, _rest::binary>> -> "application/octet-stream"
      <<0x42, 0x4D, _rest::binary>> -> "image/bmp"
      <<0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, _rest::binary>> -> "image/png"
      <<0xFF, 0xD8, 0xFF, _rest::binary>> -> "image/jpg"
      <<0x47, 0x49, 0x46, _rest::binary>> -> "image/gif"
      _ -> nil
    end
  end

  @spec verify(binary(), String.t()) :: {:ok | :error, String.t()}
  def verify(file_binary, extension) do
    with type1 when not is_nil(type1) <- FileSniffer.type_from_extension(extension),
         type2 when not is_nil(type2) <- FileSniffer.type_from_binary(file_binary),
         true <- type1 == type2 do
      {:ok, type1}
    else
      _ -> {:error, "Warning, file format and file extension do not match."}
    end
  end
end
