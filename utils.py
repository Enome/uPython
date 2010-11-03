try:
    import sys
    import clr

    #Media
    clr.AddReference('cms')
    clr.AddReference('businesslogic')
    from umbraco.cms.businesslogic.media import Media

    # Nodes
    def get_property(node, *args):
        '''
            Return None if the property value isn't define or if the value is None.
            Media uses getProperty instead of GetProperty so this doesn't work for Media
            nodes yet.
            
            updated: 
                You can now get multiple properties and it will return a tuple

            Example:
                start, middle, end = get_property( foo_node, 'start', 'middle', 'end' )
        '''
        property_values = []

        for property in args:
            if node.GetProperty(property) and node.GetProperty(property).Value:
                property_values.append( node.GetProperty(property).Value )
            else:
                property_values.append( None )
                
        
        if len( property_values ) == 1:
            return property_values[0]

        return tuple( property_values )

    #Traversing
    def find_nodes(nodes, criteria=lambda x: True):
        """
            Find nodes in a node collection by passing a filter function.
        """
        
        
        def traverse(ns):
            """
                Traverse through a collection.
            """
            
            for child in ns:
                if criteria(child): lostAndFound.append(child)
                traverse(child.Children)
    
        lostAndFound = []
        traverse(nodes)
            
        return lostAndFound
    
    def get_recursive_value(prop, id):
        id = int( id )
        path = Node( id ).Path
        
        for parentId in path.split(','):
            parentNode = Node( int( parentId ) )
            
            if parentNode.GetProperty(prop):
                return parentNode.GetProperty(prop).Value
            
        return None

    # Media
    def get_media_folder(node, property):
        '''
            return Media only if it's a umbraco media folder
        '''

        media_id = get_property(node, property)
        media_node = Media( int( media_id ) )        

        if media_node.ContentType.Text == 'Folder':
            return media_node

        return None

    def get_images_from_folder(node):
        '''
            Return tuple(name, path) from parent Media node where content type equals 'Image'
        ''' 
        if node.ContentType.Text != 'Folder':
            raise Exception('''Parent node is not of Type 'Folder' ''')

        images = []
        for image in node.Children:
            image = Media( image.Id )
    
            if image.ContentType.Text == 'Image':
                images.Add( (image.Text, image.getProperty('umbracoFile').Value ) )
            
        return images
        
        
    # Templates
    def li_a():
        return '''
            <li class='{clss}'>
                <a title='{name}' href='{url}'>
                    {name} 
                </a>
            </li>
        '''

    def img():
        return '''
            <img alt='{alt}' src='{path}' />
        '''

    def a():
        return '''
            <a title='{name}' href='{url}'>{name}</a>
        '''

except:
  print sys.exc_info()