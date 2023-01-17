# 
def normalize(x): 
    """
    Normalize the tensor on 0-1 scale
    """
    return (x-x.min()) / (x.max()-x.min())


def tensor_to_numpy_images(tensor_images):
    """
    Convert a torch tensor of shape(batch_size,channels,width,height)
    to numpy array of shape (batch_size, width, height, channels)
    
    """
    tensor_images = tensor_images.permute(0,2,3,1)
    
    if(tensor_images.requires_grad):
        tensor_images = tensor_images.detach()
        
    return tensor_images.numpy()
