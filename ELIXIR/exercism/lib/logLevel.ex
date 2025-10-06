defmodule LogLevel do
  @moduledoc """
  Case (cond) and atoms
  """
  @doc """
  Log code	Log label	Supported in legacy apps?
  0	trace	no
  1	debug	yes
  2	info	yes
  3	warning	yes
  4	error	yes
  5	fatal	no
  other / not supported	unknown	-
  """
  @spec to_label(integer(), boolean()) :: atom()
  def to_label(level, legacy?) do
    case {level, legacy?} do
      {0, false} -> :trace
      {1, _} -> :debug
      {2, _} -> :info
      {3, _} -> :warning
      {4, _} -> :error
      {5, false} -> :fatal
      _ -> :unknown
    end
  end

  @spec alert_recipient(integer(), boolean()) :: atom() | boolean()
  def alert_recipient(level, legacy?) do
    label = LogLevel.to_label(level, legacy?)

    cond do
      label == :error or label == :fatal -> :ops
      label == :unknown and legacy? -> :dev1
      # checks one by one so not legacy? is not necessary
      label == :unknown and not legacy? -> :dev2
      true -> false
    end
  end
end
