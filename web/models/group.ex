defmodule Creep.Group do
  use Creep.Web, :model

  @primary_key {:id, Ecto.UUID, autogenerate: true}
  schema "boards" do
    field :name, :string

    timestamps
  end

  @required_fields ~w(name)
  @optional_fields ~w()

  def changeset(model, params \\ :empty) do
    model
    |> cast(params, @required_fields, @optional_fields)
  end

end
