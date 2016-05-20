defmodule Creep.Board do
  use Creep.Web, :model

  alias __MODULE__

  @primary_key {:id, Ecto.UUID, autogenerate: true}
  @derive {Poison.Encoder, only: [:id, :name, :user]}
  schema "boards" do
    field :name, :string
    belongs_to :user, User

    timestamps
  end

  @required_fields ~w(name, user_id)
  @optional_fields ~w()

  def changeset(model, params \\ :empty) do
    model
    |> cast(params, @required_fields, @optional_fields)
  end

end
