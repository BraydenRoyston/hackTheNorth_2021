//
//  APIRequest.swift
//  lyricalculus
//
//  Created by Brayden Royston on 2021-09-18.
//

import UIKit

struct Book: Decodable {

    // MARK: - Properties

    let title: String
    let author: String

}

let url = URL(string: "https://bit.ly/3sspdFO")!

var request = URLRequest(url: url)

request.setValue("application/json", forHTTPHeaderField: "Content-Type")

let task = URLSession.shared.dataTask(with: url) { data, response, error in
    if let data = data {
        if let books = try? JSONDecoder().decode([Book].self, from: data) {
            print(books)
        } else {
            print("Invalid Response")
        }
    } else if let error = error {
        print("HTTP Request Failed \(error)")
    }
}
