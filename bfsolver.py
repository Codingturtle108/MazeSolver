def bfs(queue,target):
    while not queue.empty():
        pixel=queue.get()
        print(pixel.cord)
        valid_neighbours = [cell for cell in pixel.neighbours if cell is not None]
        for cell in valid_neighbours:
            if cell.cord == target and cell.visited == 0:
                cell.parent = pixel
                print('Success In Generating Path')
                path = [cell.cord]
                while cell.parent != cell:
                    cell = cell.parent
                    print(cell,cell.parent,cell.cord)
                    path.append(cell.cord)
                path.reverse()  # Reverse the path to have it from start to target
                print(path)
                return path
            if cell.visited == 0 and sum(cell.color) != 0:
                queue.put(cell)
                cell.parent = pixel
                cell.visited = 0.5
            pixel.visited = 1
    return None