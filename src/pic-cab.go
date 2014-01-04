package main

import (
	"html/template"
	"net/http"
	"github.com/gorilla/mux"
)

type Page struct {
	Title string
}

func handler(w http.ResponseWriter, r *http.Request) {
	title := r.URL.Path
	t, _ := template.ParseFiles("index.html")
	p := &Page{Title: title}
	t.Execute(w, p)	
  }

func main() {
	static_server := http.FileServer(http.Dir("./"))
	router := mux.NewRouter()
	router.PathPrefix("/assets/").Handler(static_server)
	router.HandleFunc("/", handler)
	http.Handle("/", router)
	http.ListenAndServe(":8080", nil)
}

