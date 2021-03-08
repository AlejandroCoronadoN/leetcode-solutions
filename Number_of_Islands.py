class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    """ Find all the different Islands in a 2D maytrix.
    Each piece of land is marked by the number 1 while the water is marked by 0s.
    Each island can be formed by many pieces of land connected horizontally and
    vertically.
    
    ! Considere the case where we only have one row

    Args:
        grid (List[List[str]]): [description]

    Returns:
        int: [description]
        
    """
    counter =0
    row = 0
    column=0 
    while row <= len(grid) -1:
      while column <= len(grid)-1:
        current_element = grid[row][column]
        if current_element == "1":
          #Piece of land, lets check if tehre is something arround it
          #TODO change name   to something more significant
          #self.explore_island(grid, row, column+1, captain = 'left')
          #self.explore_island(grid, row-1, column, captain = 'up')
          grid[row][column] ="2"
          counter+=1
          self.explore_island(grid, row, column-1)
          #self.explore_island(grid, row+1, column, captain = 'down')
          #TODO delete down and right -. already checked
        column+=1
      column =0
      row+=1   
    return counter
          
           
  def explore_island(self, grid, row, column, captain):
    if row >= len(grid) and column >= len(grid):
      return
    else:
      if grid[row][column] != "0" :
        if grid[row][column+1] == "1": # is land
          grid[row][column+1] = "2"
          self.explore_island(grid, row, column+1)
          
        if grid[row][column-1] == "1": # is land
          grid[row][column-1] = "2" # is land
          
          self.explore_island(grid, row, column-1)

        if grid[row+1][column] == "1": # is land
          grid[row+1][column] ="2"          
          self.explore_island(grid, row+1, column)

        if grid[row-1][column] == "1": # is land
          grid[row-1][column] ="2"
          self.explore_island(grid, row-1, column)

      