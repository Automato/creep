package main

import (
	"html/template"
	"net/http"
	"github.com/gorilla/mux"
)

type Page struct {
	Title string
}

func DefaultHandler(w http.ResponseWriter, r *http.Request) {
	title := r.URL.Path
	t, _ := template.ParseFiles("index.html")
	p := &Page{Title: title}
	t.Execute(w, p)	
  }

func main() {

	// Static file server to operate on the directory that calls it
	static_server := http.FileServer(http.Dir("./"))
	
	// A multiplexing router to handle requests
	router := mux.NewRouter()
	
	// Setup routes here
	router.PathPrefix("/assets/").Handler(static_server) // will serve assets folder
	router.HandleFunc("/", DefaultHandler) // Fallthrough to DefaultHandler
	
	// Serve the multiplexer
	http.Handle("/", router)
	http.ListenAndServe(":8080", nil)
}

