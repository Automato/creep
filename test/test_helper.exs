ExUnit.start

Mix.Task.run "ecto.create", ~w(-r Creep.Repo --quiet)
Mix.Task.run "ecto.migrate", ~w(-r Creep.Repo --quiet)
Ecto.Adapters.SQL.begin_test_transaction(Creep.Repo)

