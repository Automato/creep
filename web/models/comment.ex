defmodule Creep.Comment do
  use Creep.Web, :model

  alias __MODULE__

  @primary_key {:id, Ecto.UUID, autogenerate: true}
  @derive {Poison.Encoder, only: [:id, :name, :user]}
  schema "comments" do
    field :content, :string

    belongs_to :card, Card
    belongs_to :user, User

    timestamps
  end

  @required_fields ~w(content card_id user_id)
  @optional_fields ~w()

  def changeset(model, params \\ :empty) do
    model
    |> cast(params, @required_fields, @optional_fields)
  end

end
