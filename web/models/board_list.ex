defmodule Creep.BoardList do
  use Creep.Web, :model

  alias __MODULE__

  @primary_key {:id, Ecto.UUID, autogenerate: true}
  @derive {Poison.Encoder, only: [:id, :name, :user]}
  schema "board_lists" do
    field :name, :string

    has_many :board, Board

    belongs_to :user, User
    belongs_to :group, Group

    timestamps
  end

  @required_fields ~w(name)
  @optional_fields ~w(group_id user_id)

  def changeset(model, params \\ :empty) do
    model
    |> cast(params, @required_fields, @optional_fields)
  end

end
