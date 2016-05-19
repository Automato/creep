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
  end

  scope "/", Creep do
    pipe_through :browser # Use the default browser stack

    get "/", PageController, :index
  end

  scope "/api", Creep do
     pipe_through :api

     scope "v1" do
       post "/registrations", RegistrationController, :create
     end
   end
end
