//
//  User.swift
//  Cal Poly Cat Program App
//
//  Created by Jillian Quinn on 6/7/20.
//  Copyright © 2020 Hack4Impact. All rights reserved.
//
// Models/User.swift
         
import Foundation
                             
struct User:Decodable{
    static var current:User!
    var token:String
    
}
