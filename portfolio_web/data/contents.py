import reflex as rx
from dataclasses import dataclass
from typing import List


@dataclass
class CodeSnippet:
    code: str
    language: str


@dataclass
class BlogPost:
    id: str
    title: str
    date: str
    preview: str
    content: str
    tags: List[str]
    reading_time: str
    code_blocks: List[CodeSnippet] = None


@dataclass
class BlogPost:
    def __init__(
        self,
        id: str,  # Add unique ID
        title: str,
        date: str,
        preview: str,
        content: str,
        tags: list[str],
        reading_time: str,
        code_blocks: list[CodeSnippet] = None,
    ):
        self.id = id
        self.title = title
        self.date = date
        self.preview = preview
        self.content = content
        self.tags = tags
        self.reading_time = reading_time
        self.code_blocks = code_blocks or []


print("Creating blog posts list:")
blog_posts = [
    BlogPost(
        id="drug-discovery-ai",
        title="Revolutionizing Drug Discovery with Generative AI",
        date="March 15, 2024",
        reading_time="8 mins",
        preview="Exploring how our latest deep learning model achieved 87% accuracy in predicting protein-ligand interactions...",
        tags=["AI", "Drug Discovery", "Research"],
        content="""### The Challenge in Drug Discovery,
      

Traditional drug discovery is like finding a needle in a haystack - expensive, time-consuming, and often frustrating. But what if AI could help us find that needle faster?

### Our Approach
We've developed a novel deep learning architecture that combines:
- Transformer-based protein sequence analysis
- Graph neural networks for molecular structure understanding
- Attention mechanisms for binding site prediction

### Key Results
Our model achieved:
- 87% accuracy in protein-ligand interaction prediction
- 60% reduction in computational screening time
- 3x improvement in hit rate compared to traditional methods""",
        code_blocks=[
            CodeSnippet(
                language="python",
                code="""import torch
import torch.nn as nn

class DrugDiscoveryModel(nn.Module):
  def __init__(self, input_dim, hidden_dim):
      super().__init__()
      self.encoder = nn.Sequential(
          nn.Linear(input_dim, hidden_dim),
          nn.ReLU(),
          nn.Linear(hidden_dim, hidden_dim)
      )
  
  def forward(self, x):
      return self.encoder(x)""",
            )
        ],
    ),
    BlogPost(
        id="self-attention-pytorch",
        title="Self-Attention in Deep Learning",
        date="March 20, 2024",
        reading_time="12 mins",
        preview="A deep dive into implementing self-attention mechanisms with practical PyTorch code examples...",
        tags=["PyTorch", "Deep Learning", "Code Tutorial"],
        content="""### Understanding Self-Attention

Self-attention is a crucial component in modern deep learning architectures. Let's implement it step by step.""",
        code_blocks=[
            CodeSnippet(
                language="python",
                code="""import torch
import torch.nn as nn

class SelfAttention(nn.Module):
  def __init__(self, embed_size, heads):
      super(SelfAttention, self).__init__()
      self.embed_size = embed_size
      self.heads = heads
      self.head_dim = embed_size // heads

      self.queries = nn.Linear(embed_size, embed_size)
      self.keys = nn.Linear(embed_size, embed_size)
      self.values = nn.Linear(embed_size, embed_size)
      self.fc_out = nn.Linear(embed_size, embed_size)

  def forward(self, query, key, value, mask=None):
      N = query.shape[0]
      value_len, key_len, query_len = value.shape[1], key.shape[1], query.shape[1]

      # Split embedding into self.heads pieces
      queries = self.queries(query).reshape(N, query_len, self.heads, self.head_dim)
      keys = self.keys(key).reshape(N, key_len, self.heads, self.head_dim)
      values = self.values(value).reshape(N, value_len, self.heads, self.head_dim)

      energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
      if mask is not None:
          energy = energy.masked_fill(mask == 0, float("-1e20"))

      attention = torch.softmax(energy / (self.embed_size ** (1/2)), dim=3)
      out = torch.einsum("nhql,nlhd->nqhd", [attention, values])
      
      out = out.reshape(N, query_len, self.embed_size)
      return self.fc_out(out)""",
            ),
            CodeSnippet(
                language="python",
                code="""# Example usage
attention = SelfAttention(embed_size=256, heads=8)
x = torch.randn(32, 10, 256)  # batch_size=32, seq_len=10, embed_size=256
output = attention(x, x, x)  # self-attention
print(output.shape)  # torch.Size([32, 10, 256])""",
            ),
        ],
    ),
    BlogPost(
        id="bio-image-analysis",
        title="Breaking Down Our Latest Paper on Bio-Image Analysis",
        date="February 20, 2024",
        reading_time="10 mins",
        preview="A behind-the-scenes look at how we developed a novel CNN architecture that achieves state-of-the-art performance...",
        tags=["Deep Learning", "Research", "Publication"],
        content="""### Breaking Down Our Research
In our latest paper, we present a novel approach to bio-image analysis that combines attention mechanisms with traditional CNN architectures. Let's dive into the technical details.

### Visualization of Attention Weights
Here's a heatmap showing how our attention mechanism focuses on different regions of biological images:

![Attention Heatmap](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fnmeth.1902/MediaObjects/41592_2012_Article_BFnmeth1902_Fig1_HTML.jpg?as=webp)

### Performance Analysis
Our model shows significant improvements over baseline approaches. The training curves below demonstrate stable convergence and strong generalization.

### Video Explanation
Watch our detailed walkthrough of the architecture and results:

<iframe 
  width="100%" 
  height="400" 
  src="https://www.youtube.com/embed/Y63VW5emBx4" 
  frameborder="0" 
  allowfullscreen>
</iframe>""",
        code_blocks=[
            CodeSnippet(
                language="python",
                code="""import torch
import torch.nn as nn

class SelfAttention(nn.Module):
  def __init__(self, embed_size, heads):
      super(SelfAttention, self).__init__()
      self.embed_size = embed_size
      self.heads = heads
      self.head_dim = embed_size // heads

      self.queries = nn.Linear(embed_size, embed_size)
      self.keys = nn.Linear(embed_size, embed_size)
      self.values = nn.Linear(embed_size, embed_size)
      self.fc_out = nn.Linear(embed_size, embed_size)

  def forward(self, query, key, value, mask=None):
      N = query.shape[0]
      value_len, key_len, query_len = value.shape[1], key.shape[1], query.shape[1]

      # Split embedding into self.heads pieces
      queries = self.queries(query).reshape(N, query_len, self.heads, self.head_dim)
      keys = self.keys(key).reshape(N, key_len, self.heads, self.head_dim)
      values = self.values(value).reshape(N, value_len, self.heads, self.head_dim)

      # Scaled dot-product attention
      energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
      if mask is not None:
          energy = energy.masked_fill(mask == 0, float("-1e20"))

      attention = torch.softmax(energy / (self.embed_size ** (1/2)), dim=3)
      out = torch.einsum("nhql,nlhd->nqhd", [attention, values])
      
      out = out.reshape(N, query_len, self.embed_size)
      return self.fc_out(out)""",
            ),
            CodeSnippet(
                language="python",
                code="""# Example usage and performance metrics
import matplotlib.pyplot as plt
import numpy as np

# Training history
epochs = np.arange(1, 6)
train_acc = np.array([0.6, 0.7, 0.8, 0.85, 0.88])
val_acc = np.array([0.55, 0.65, 0.75, 0.78, 0.80])

plt.figure(figsize=(10, 6))
plt.plot(epochs, train_acc, 'b-', label='Training Accuracy')
plt.plot(epochs, val_acc, 'r-', label='Validation Accuracy')
plt.title('Model Performance')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)""",
            ),
        ],
    ),
    BlogPost(
        id="unet-medical-image-segmentation",
        title="Biomedical Image Segmentation with U-Net",
        date="March 15, 2024",
        reading_time="15 mins",
        preview="Implementation and analysis of U-Net architecture for medical image segmentation...",
        tags=["Medical AI", "Computer Vision", "PyTorch"],
        content="""### U-Net Architecture for Medical Image Segmentation
We'll explore implementing a U-Net model for biomedical image segmentation, including the architecture, training process, and performance analysis.

### Architecture Overview
The U-Net consists of an encoder path (left side) and a decoder path (right side), connected by skip connections.""",
        code_blocks=[
            CodeSnippet(
                language="python",
                code="""import torch
import torch.nn as nn
import torch.nn.functional as F

class UNet(nn.Module):
  def __init__(self, in_channels=1, out_channels=1):
      super(UNet, self).__init__()
      
      # Encoder
      self.enc1 = self.conv_block(in_channels, 64)
      self.enc2 = self.conv_block(64, 128)
      self.enc3 = self.conv_block(128, 256)
      self.enc4 = self.conv_block(256, 512)
      
      # Decoder
      self.up3 = self.up_conv(512, 256)
      self.dec3 = self.conv_block(512, 256)
      self.up2 = self.up_conv(256, 128)
      self.dec2 = self.conv_block(256, 128)
      self.up1 = self.up_conv(128, 64)
      self.dec1 = self.conv_block(128, 64)
      self.final = nn.Conv2d(64, out_channels, kernel_size=1)

  def forward(self, x):
      # Encoding
      enc1 = self.enc1(x)
      enc2 = self.enc2(F.max_pool2d(enc1, 2))
      enc3 = self.enc3(F.max_pool2d(enc2, 2))
      enc4 = self.enc4(F.max_pool2d(enc3, 2))
      
      # Decoding
      dec3 = self.dec3(torch.cat([self.up3(enc4), enc3], dim=1))
      dec2 = self.dec2(torch.cat([self.up2(dec3), enc2], dim=1))
      dec1 = self.dec1(torch.cat([self.up1(dec2), enc1], dim=1))
      
      return torch.sigmoid(self.final(dec1))

  def conv_block(self, in_ch, out_ch):
      return nn.Sequential(
          nn.Conv2d(in_ch, out_ch, 3, padding=1),
          nn.BatchNorm2d(out_ch),
          nn.ReLU(inplace=True),
          nn.Conv2d(out_ch, out_ch, 3, padding=1),
          nn.BatchNorm2d(out_ch),
          nn.ReLU(inplace=True)
      )

  def up_conv(self, in_ch, out_ch):
      return nn.ConvTranspose2d(in_ch, out_ch, 2, stride=2)""",
            ),
            CodeSnippet(
                language="python",
                code="""# Training setup
def train_model(model, train_loader, criterion, optimizer):
  model.train()
  for batch_idx, (data, target) in enumerate(train_loader):
      optimizer.zero_grad()
      output = model(data)
      loss = criterion(output, target)
      loss.backward()
      optimizer.step()
      
  return loss.item()""",
            ),
        ],
    ),
    BlogPost(
        id="generative-ai-drug-discovery",
        title="Generative AI for Drug Discovery",
        date="March 5, 2024",
        reading_time="8 mins",
        preview="Using generative models to accelerate drug discovery pipeline...",
        tags=["Drug Discovery", "Generative AI", "Chemistry"],
        content="""### Molecular Generation with VAE
We present a Variational Autoencoder (VAE) approach for generating novel molecular structures.""",
        code_blocks=[
            CodeSnippet(
                language="python",
                code="""import torch
import torch.nn as nn

class MolecularVAE(nn.Module):
  def __init__(self, input_dim, latent_dim):
      super().__init__()
      # Encoder
      self.encoder = nn.Sequential(
          nn.Linear(input_dim, 512),
          nn.ReLU(),
          nn.Linear(512, 256)
      )
      self.fc_mu = nn.Linear(256, latent_dim)
      self.fc_var = nn.Linear(256, latent_dim)
      
      # Decoder
      self.decoder = nn.Sequential(
          nn.Linear(latent_dim, 256),
          nn.ReLU(),
          nn.Linear(256, 512),
          nn.ReLU(),
          nn.Linear(512, input_dim),
          nn.Sigmoid()
      )
  
  def encode(self, x):
      h = self.encoder(x)
      return self.fc_mu(h), self.fc_var(h)
      
  def reparameterize(self, mu, log_var):
      std = torch.exp(0.5 * log_var)
      eps = torch.randn_like(std)
      return mu + eps * std
      
  def forward(self, x):
      mu, log_var = self.encode(x)
      z = self.reparameterize(mu, log_var)
      return self.decoder(z), mu, log_var""",
            )
        ],
    ),
    BlogPost(
        id="attention-mechanisms-pytorch",
        title="Implementing Attention Mechanisms in PyTorch",
        date="March 20, 2024",
        reading_time="12 mins",
        preview="A deep dive into implementing self-attention mechanisms with practical PyTorch code examples...",
        tags=["PyTorch", "Deep Learning", "Code Tutorial"],
        content="""
### Self-Attention Implementation in PyTorch

Below is a clean implementation of the self-attention mechanism:
""",
        code_blocks=[
            CodeSnippet(
                language="python",
                code="""import torch
import torch.nn as nn

class SelfAttention(nn.Module):
  def __init__(self, embed_size, heads):
      super(SelfAttention, self).__init__()
      self.embed_size = embed_size
      self.heads = heads
      self.head_dim = embed_size // heads

      self.queries = nn.Linear(embed_size, embed_size)
      self.keys = nn.Linear(embed_size, embed_size)
      self.values = nn.Linear(embed_size, embed_size)
      self.fc_out = nn.Linear(embed_size, embed_size)

  def forward(self, query, key, value, mask=None):
      N = query.shape[0]
      value_len, key_len, query_len = value.shape[1], key.shape[1], query.shape[1]

      # Split embedding into self.heads pieces
      queries = self.queries(query).reshape(N, query_len, self.heads, self.head_dim)
      keys = self.keys(key).reshape(N, key_len, self.heads, self.head_dim)
      values = self.values(value).reshape(N, value_len, self.heads, self.head_dim)

      # Scaled dot-product attention
      energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
      if mask is not None:
          energy = energy.masked_fill(mask == 0, float("-1e20"))

      attention = torch.softmax(energy / (self.embed_size ** (1/2)), dim=3)
      out = torch.einsum("nhql,nlhd->nqhd", [attention, values])
      
      out = out.reshape(N, query_len, self.embed_size)
      return self.fc_out(out)""",
            ),
            CodeSnippet(
                language="python",
                code="""# Example usage
attention = SelfAttention(embed_size=256, heads=8)
x = torch.randn(32, 10, 256)  # batch_size=32, seq_len=10, embed_size=256
output = attention(x, x, x)  # self-attention
print(output.shape)  # torch.Size([32, 10, 256])""",
            ),
        ],
    ),
    BlogPost(
        id="custom-css-reflex",
        title="Advanced CSS in Reflex",
        date="March 15, 2024",
        reading_time="8 mins",
        preview="Learn how to style your Reflex components with advanced CSS techniques...",
        tags=["CSS", "Reflex", "Web Development"],
        content="""
### Styling Reflex Components

Here's how to create custom styled components:
""",
        code_blocks=[
            CodeSnippet(
                language="css",
                code="""/* Custom CSS styles */
.custom-button {
  background: linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%);
  border-radius: 3px;
  border: 0;
  color: white;
  padding: 0 30px;
  box-shadow: 0 3px 5px 2px rgba(255, 105, 135, .3);
}""",
            ),
            CodeSnippet(
                language="python",
                code="""import reflex as rx

def custom_button(text: str) -> rx.Component:
  return rx.box(
      rx.button(
          text,
          class_name="custom-button",
          _hover={
              "transform": "scale(1.05)",
              "transition": "transform 0.2s",
          }
      )
  )""",
            ),
        ],
    ),
]

print(f"Created {len(blog_posts)} blog posts")
