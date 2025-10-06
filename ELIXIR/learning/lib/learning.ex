# structs
defmodule Membership do
  defstruct [:type, :price]
end

defmodule User do
  defstruct [:name, :membership]
end

# the actual class or function set
defmodule Learning do
  @moduledoc """
  Documentation for `Learning`.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Learning.hello()
      :world

  """
  use Application

  @x 5 # works like a constant - immutable variable

  alias UUID

  def start(_type, _args) do
    # code
    Learning.main()
    # execution
    Supervisor.start_link([], strategy: :one_for_one) # works so that you can just run without specifying function
  end

  def main do
    y = 10
    IO.puts(@x + y)
    IO.puts(:hello) # static ATOMS -> constant value that is hardcoded. not good for user input
    #IO.puts()
    IO.inspect(Learning.sumAndAverage([1, 2, 3, 4, 5]))
  end

  def stringExample do
    name = "Anna"
    # https://hexdocs.pm/elixir/Enum.html
    status = Enum.random([:gold, :silver, :bronze])

    if status == :gold do
      IO.puts("Welcome to gold status, #{name}")
    else
      IO.puts("Get lost") # returns ok as well because no explicit return value in this function
    end
  end

  def caseExample do # example on cases
    name = "Anna"
    status = Enum.random([:gold, :silver, :bronze])
    case status do
      :gold -> IO.puts("Welcome to gold status, #{name}")
      :silver -> IO.puts("Welcome to silver status, #{name}")
      _ -> IO.puts("The rest of the cases here")
    end
  end

  def moreStringExample do
    # https://hexdocs.pm/elixir/String.html
    IO.puts("This\nis\na\nmessage\n")
    IO.puts("After")
    IO.puts("Interpolation looks like \#{}") # quite literally puts #{}
    IO.puts(?a) # value of 97 -> character value
  end

  def numbersExample do
    a = 10
    b = 3.0 # no difference between float and double in elixir
    c = 5
    IO.puts(a + b)
    IO.puts(a / c) # division always returns a float.
    :io.format("~.20f\n", [0.1]) # 20 spots after the decimal - 0.1 cannot be represented perfectly
    IO.puts(Float.ceil(3.5, 1)) # Float can access all float libraries. this is ceil up to the 1st decimal spot
  end

  def timeExample do
    time = Time.new!(16, 30, 0, 0) # hour minute seconds millisecond
    date = Date.new!(2025, 1, 1)
    dateTime = DateTime.new!(date, time, "Etc/UTC") # add new with ! to throw an error or go past compiling error
    IO.inspect(dateTime)
  end

  def appExample do
    time = DateTime.new!(Date.new!(2025, 1, 1), Time.new!(0, 0, 0, 0), "Etc/UTC")
    timeUntil = DateTime.diff(time, DateTime.utc_now())
    IO.puts(timeUntil)

    days = div(timeUntil, 86_400) # or timeUntil / 86_400
    IO.puts(days)
    hours = div((rem(timeUntil, 86_400)), 60 * 60) # underscores dont interrupt the number but make them more readable
    IO.puts(hours)
    mins = div(rem(timeUntil, 60 * 60), 60)
    IO.puts(mins)
    secs = rem(timeUntil, 60)
    IO.puts(secs)

    IO.puts("Time until new year: #{days} days, #{hours}, hours, #{mins} minutes, #{secs}, seconds.")
  end

  def tupleExample do
    memberships = {:bronze, :silver}
    memberships = Tuple.append(memberships, :gold) # deprecated, user insert_at instead
    IO.inspect(memberships)

    prices = {5, 10, 15}
    avg = Tuple.sum(prices) / tuple_size(prices)
    IO.puts(avg)

    IO.puts("Average price from #{elem(memberships, 0)} #{elem(memberships, 1)} #{elem(memberships, 2)} is #{avg}")

    user1 = {"Anna", :silver} # can mix types inside a tuple
    user2 = {"Mieko", :bronze}
    user3 = {"Thao", :gold}

    {name, membership} = user1 # tuple of size 2, set variables name and membership

    IO.puts("#{name} has a #{membership} membership.")

    # at this point it might be better to use a list and do loops
    users = [{"Anna", :silver},{"Mieko", :bronze},{"Thao", :gold}]
    Enum.each(users, fn {name, membership} ->
      IO.puts("#{name} has a #{membership} membership.")
    end)
  end

  def mapExample do
    prices = %{gold: 25, silver: 20, bronze: 15, none: 0}
    users = [{"Anna", :silver},{"Mieko", :bronze},{"Thao", :gold}]
    Enum.each(users, fn {name, membership} ->
      IO.puts("#{name} has a #{membership} membership and they are paying #{prices[membership]}.") # can also call like -> prices.gold
    end)
  end

  def structExample do
    goldMembership = %Membership{type: :gold, price: 25}
    silverMembership = %Membership{type: :silver, price: 25}
    bronzeMembership = %Membership{type: :bronze, price: 25}
    noneMembership = %Membership{type: :none, price: 25}

    users = [%User{name: "Anna", membership: silverMembership}, %User{name: "Mieko", membership: bronzeMembership}, %User{name: "Thao", membership: goldMembership}]

    Enum.each(users, fn %User{name: name, membership: membership} ->
      IO.puts("#{name} has a #{membership.type} membership and they are paying #{membership.price}.")
    end)
  end

  def guessingGame do
    correct = :rand.uniform(11) - 1 # get a random number from 1 to 10
    guess = IO.gets("Guess a number between 0 and 10: ") |> String.trim() # trims any whitespace or newline
    IO.puts("The correct answer was #{correct}, you guessed #{guess}")
    if String.to_integer(guess) == correct do # convert string input into integer for comparison
      IO.puts("You win")
    else
      IO.puts("You lose")
    end
  end

  def guessingGame2 do
    correct = :rand.uniform(11) - 1 # get a random number from 1 to 10
    guess = IO.gets("Guess a number between 0 and 10: ") |> String.trim() |> Integer.parse()
    IO.inspect(guess) #(would output {5, ""})
    #IO.puts(elem(guess, 0)) #(this gets just t guessed element)

    case guess do
      {result, ""} -> IO.puts("parse successful #{result}")
      {result, other} -> IO.puts("parse partially successful #{result} and #{other}")

      # or {result, _} -> IO.puts("parse successful #{result})
      # add the if statement here for successful parsing
      :error -> IO.puts("Something went wrong")
    end
  end

  def listComprehensionExample do
    grades = [25, 50, 75, 100]
    new = for n <- grades, do: n + 5
    IO.inspect(new)

    # adding new data
    new = new ++ [125]
    new = new ++ [150, 175] # add ot the end
    new = [5 | new] # add to the beginning
    IO.inspect(new)

    # even = for n <- new, <condition>, do: n
    even = for n <- new, rem(n, 2) == 0, do: n # or Integer.is_even(n)
    IO.inspect(even)
  end

  def functionalProgrammingExample do
    numbers = [1, 2, 3, 4, 5]
    Enum.each(numbers, fn num -> IO.puts(num) end) # anonymous function

    # convert all number into strings
    result = Enum.map(numbers, &Integer.to_string/1) #& changes non anon function into an anonymous one
    IO.inspect(result)
  end

  def sumAndAverage(numbers) do
    sum = Enum.sum(numbers)
    average = sum / Enum.count(numbers)
    {sum, average} # return value
  end

  def printNumbers(numbers) do
    numbers |> Enum.join(" ") |> IO.puts() # no return value
  end
end
