defmodule Newsletter do
  @moduledoc """
  File
  Functions for working with files are provided by the File module.

  To read a whole file, use File.read/1. To write to a file, use File.write/2.

  Every time a file is written to with File.write/2, a file descriptor is opened and a new Elixir process is spawned.
  For this reason, writing to a file in a loop using File.write/2 should be avoided.

  Instead, a file can be opened using File.open/2.
  The second argument to File.open/2 is a list of modes, which allows you to specify if you want to open the file for reading or for writing.

  File.open/2 returns a PID of a process that handles the file.
  To read and write to the file, use functions from the IO module and pass this PID as the IO device.

  When you're finished working with the file, close it with File.close/1.

  All the mentioned functions from the File module also have a ! variant that raises an error instead of returning an error tuple
  (e.g. File.read!/1). Use that variant if you don't intend to handle errors such as missing files or lack of permissions.
  """
  def read_emails(path) do
    File.read!(path)
    # handles newline for both Unix and Windows
    |> String.split(~r/\r?\n/, trim: true)
    # removes empty strings from the ends (safety)
    |> Enum.filter(&(&1 != ""))
  end

  def open_log(path) do
    File.open!(path, [:write])
  end

  def log_sent_email(pid, email) do
    IO.puts(pid, email)
  end

  def close_log(pid) do
    File.close(pid)
  end

  def send_newsletter(emails_path, log_path, send_fun) do
    emails_list = Newsletter.read_emails(emails_path)
    log_pid = Newsletter.open_log(log_path)

    Enum.each(emails_list, fn email ->
      if send_fun.(email) == :ok do
        Newsletter.log_sent_email(log_pid, email)
      end
    end)

    close_log(log_pid)
  end
end
