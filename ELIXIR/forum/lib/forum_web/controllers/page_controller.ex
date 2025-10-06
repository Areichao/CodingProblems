defmodule ForumWeb.PageController do
  use ForumWeb, :controller

  def home(conn, _params) do
    # The home page is often custom made,
    # so skip the default app layout.
    render(conn, :home, layout: false)
  end

  # new function for new page
  def users(conn, _params) do
    IO.puts("Users function hit!")
    users = [
      %{id: 1, name: "Alice", email: "alice@email.com"},
      %{id: 2, name: "Bob", email: "bob@email.com"}
    ]

    json(conn, %{users: users}) # returning json data
    # render(conn, :users, users: users, layout: false) # version of not returning json data
    # https://hexdocs.pm/eex/1.12.3/EEx.html
  end
end
