defmodule Creep.Card do
  use Creep.Web, :model

  @primary_key {:id, Ecto.UUID, autogenerate: true}
  @derive {Poison.Encoder, only: [:id, :name, :points, :user]}
  schema "cards" do
    field :name, :string
    field :points, :integer

    has_one :created_by, Creep.User
    has_many :comments, Creep.Comment

    timestamps
  end

  @required_fields ~w(name points user_id)
  @optional_fields ~w()

  def changeset(model, params \\ :empty) do
    model
    |> cast(params, @required_fields, @optional_fields)
  end

end
