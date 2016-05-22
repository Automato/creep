defmodule Creep.List do
  use Creep,Web, :model

  alias Creep.{Board, Repo, Card}

  @primary_key {:id, Ecto.UUID, autogenerate: true}
  @derive {Poison.Encoder, only: [:id, :board_id, :name, :board_index, :cards]}
  schema "lists" do
    field :name, :string
    field :board_index, :integer

    belongs_to :board, Board
    has_many :cards, Card

    timestamps
  end

  @required_fields ~w(name)
  @optional_fields ~w(board_index)

  def changeset(model, params \\ :empty) do
    model
    |> cast(params, @required_fields, @optional_fields)
  end
end
