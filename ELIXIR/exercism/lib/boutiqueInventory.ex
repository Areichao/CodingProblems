defmodule BoutiqueInventory do
  @moduledoc """
  Enum module
  """
  def sort_by_price(inventory) do
    Enum.sort_by(inventory, fn item -> item[:price] end)
  end

  def with_missing_price(inventory) do
    Enum.filter(inventory, fn item -> item[:price] == nil end)
  end

  def update_names(inventory, old_word, new_word) do
    Enum.map(inventory, fn item ->
      Map.put(item, :name, String.replace(item[:name], old_word, new_word))
    end)
  end

  # def increase_quantity(item, count) do
  #   updated_amount = item[:quantity_by_size]
  #   |> Enum.map(fn {size, qty} -> {size, qty + count} end)
  #   |> Map.new()

  #   Map.put(item, :quantity_by_size, updated_amount)
  # end

  def increase_quantity(item, count) do
    updated_amount = Map.new(item[:quantity_by_size], fn {size, qty} -> {size, qty + count} end)
    Map.put(item, :quantity_by_size, updated_amount)
  end

  def total_quantity(item) do
    Enum.reduce(item[:quantity_by_size], 0, fn {_size, qty}, acc -> acc + qty end)
  end
end
