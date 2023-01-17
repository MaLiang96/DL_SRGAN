import matplotlib.pyplot as plt

def visulize_samples(samples):
    num_rows = 4
    num_cols = 8
    idx = 0
    
    #plt.title('Sample Images')
    for i in range(num_rows):
        for j in range(num_cols):
            ax=plt.subplot(num_rows, num_cols,idx+1)
            #plt.title('Orignal')
            plt.imshow(samples[idx])
            plt.axis('off')
            idx += 1
    plt.gcf().set_size_inches(12, 7.5)
    plt.subplots_adjust(wspace=0, hspace=0)
        
def visulize_reconstructed(orignal, reconstructed, img_size=(28,28)):
    num_samples = 3
    for i in range(num_samples):
        idx = i*2 + 1
        plt.subplot(num_samples,2,idx)
        plt.title('Orignal')
        plt.imshow(orignal[i].reshape(*img_size))
        plt.axis('off')
        idx += 1
        plt.subplot(num_samples,2,idx)
        plt.title('Reconstructed')
        plt.axis('off')
        plt.imshow(reconstructed[i].reshape(*img_size))
        plt.gcf().set_size_inches(6, 8)
        
        
def visulize_noised_reconstructed(orignal, noised, denoised, img_size=(28,28)):
    num_samples = 3
    idx=1
    for i in range(num_samples):
        plt.subplot(num_samples,3,idx)
        plt.title('Orignal')
        plt.imshow(orignal[i].reshape(*img_size))
        plt.axis('off')
        idx += 1
        
        plt.subplot(num_samples,3,idx)
        plt.title('Noised')
        plt.axis('off')
        plt.imshow(noised[i].reshape(*img_size))
        idx += 1
        
        plt.subplot(num_samples,3,idx)
        plt.title('Denoised')
        plt.axis('off')
        plt.imshow(denoised[i].reshape(*img_size))
        idx += 1
        
        plt.gcf().set_size_inches(6, 8)
