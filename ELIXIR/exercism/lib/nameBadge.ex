defmodule NameBadge do
  @moduledoc """
  nil
  also
  if age > 16, do: "beer", else: "no beer"
  everything in elixir is true except for false
  """

  def print(id, name, department) do
    if id == nil and department != nil do
      "#{name} - #{String.upcase(department)}"
    else
      if id == nil and department == nil do
        "#{name} - OWNER"
      else
        if department == nil do
          "[#{id}] - #{name} - OWNER"
        else
          "[#{id}] - #{name} - #{String.upcase(department)}"
        end
      end
    end
  end
end
