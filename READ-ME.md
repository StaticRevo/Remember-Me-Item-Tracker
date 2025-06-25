# Remember Me – Smart Personal Storage Tracker

**Remember Me** is a mobile app that helps users efficiently organize and locate their personal belongings across rooms, shelves, and storage areas in their home. Designed for simplicity and practical use, the app enables users to map out their living space and track exactly where each item is stored.


## Description

Do you ever forget where you placed your sunglasses, your maths notes, or that one specific cable?  
**Remember Me** is a React Native app that lets you build a virtual inventory of your belongings and **remember where everything is stored**—from your wardrobe’s second shelf to a drawer in your desk.

With a searchable floor plan and item-based tagging, this app is ideal for students, homeowners, and anyone who wants to avoid the frustration of digging through every drawer.


## Features

- **Add Custom Items**
  - Add any item you want to track
  - Write a description and take an optional photo
  - Store it under a specific location path

- **Custom Rooms & Storage**
  - Define custom rooms (e.g., Bedroom 1, Garage)
  - Add sub-areas like storage zones, shelves, cabinets, etc.
  - Label and organize areas your way

- **Visual Floor Plan Map**
  - View a simplified visual representation of your house layout
  - Items are tagged to specific areas on the map

- **Smart Search**
  - Quickly find where an item is stored using a search bar
  - Automatically highlights the item’s location on the floor map

- **Efficient Organisation**
  - Designed to make your physical space searchable and logically structured
  - Great for organising notes, electronics, tools, clothes, and seasonal items


## Tech Stack

- **Frontend**: React Native (Expo)
- **Storage**: Firebase Firestore (cloud database)
- **Media**: Firebase Storage (item photos)
- **Navigation**: React Navigation
- **Map Rendering** (future): SVG or grid-based visual layout


## Example Use Case

> 📁 **Item**: *Maths Notes*  
> 📍 **Location**: Bedroom 1 → Storage Area 1 → Shelf 2  
> 🖼️ **Photo**: (attached)  
> 📃 **Description**: Old MATSEC notes from 2022  

You search for "Maths Notes", and the app tells you exactly where it is and marks its position on your room map.


## Future Improvements

- Add reminder system for borrowed items
- Floor plan designer with drag-and-drop layout
- Export inventory as PDF or CSV
- Sync with other users (e.g., shared flatmates)

