defmodule Creep.Router do
  use Creep.Web, :router

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    plug :accepts, ["json"]
    plug Guardian.Plug.VerifyHeader
    plug Guardian.Plug.LoadResource
  end

  scope "/", Creep do
    pipe_through :browser # Use the default browser stack

    get "/", PageController, :index
  end

  scope "/api", Creep do
     pipe_through :api

     scope "v1" do
       get "/me", MeController, :show
       post "/registrations", RegistrationController, :create

       # This delete is accross the collection, which is why resource is not used
       delete "/sessions", SessionController, :delete
       post "/sessions", SessionController, :create
     end
   end
end
