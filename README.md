FWS_Gitters_n_Repos
===================

A way to solve Chris' concern about managing FWS repos

history:
	20140829 - daryl van dyke - Added original code
	20140902 - daryl van dyke - updated code for HTML generation




In default configuration, the script defaults the HTML output to 'GIT_users.htm' 
in the same directory the program is run in.  

The data model is a two-position list, of two-position tuples:

[ ....  , [ ( UserName, URL_to_User_GitHub), (Repo_Name, URL_to_Repo) ], .... ]

To prettyprint the data, use positions 0 -->    listElement[0][0], listElement[1][0]
To retrieve URLs, use positions 1        -->    listElement[0][1], listElement[1][1]


This software is in the public domain.  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.